#!/bin/sh

set -e

part1() {
    ###############################################################################
    # PART I - CALLING SETUP (which will call py2app)
    
    echo
    echo "Building for Mac OSX (1 of 2)"
    echo "============================="
    echo
    echo "= Cleaning up ="
    ./clean.sh
    
    echo
    echo "= Executing python setup.py py2app ="
    python setup.py py2app #  --semi-standalone
    
    echo
    echo "= Removing source files ="
    find dist/Anamorphy.app/Contents/Resources/lib/ -name "*.py" -exec rm "{}" \;
    
    echo
    echo "= Done ="
    echo "Result: dist/Anamorphy.app"
}

part2() {
    ###############################################################################
    # PART II - BUILDING DMG (unrelated to Python)
    
    # http://stackoverflow.com/questions/96882/
    
    echo
    echo "Building DMG archive (2 of 2)"
    echo "============================="
    echo
    
    revision=$(python -c "from anamorphy_files import version; print version.getVersionFromIni()")
    
    size=100000
    source=dist/Anamorphy.app
    title=AnamorphyInstaller-${revision}
    applicationName=Anamorphy
    finalDMGName=AnamorphyInstaller-${revision}
    pack=pack.temp.dmg
    
    rm -f ${pack}
    rm -f ${finalDMGName}.dmg
    hdiutil detach /Volumes/${title} 2>/dev/null || true
    
    
    # 1. Make sure that "Enable access for assistive devices" is checked
    # in System Preferences>>Universal Access. It is required for the
    # AppleScript to work. You may have to reboot after this change (it
    # doesn't work otherwise on Mac OS X Server 10.4).
    
    
    # 2. Create a R/W DMG. It must be larger than the result will be. In
    # this example, the bash variable "size" contains the size in Kb and
    # the contents of the folder in the "source" bash variable will be
    # copied into the DMG:
    
    echo hdiutil create -srcfolder "${source}" -volname "${title}" -fs HFS+ \
          -fsargs "-c c=64,a=16,e=16" -format UDRW -size ${size}k ${pack}
    
    hdiutil create -srcfolder "${source}" -volname "${title}" -fs HFS+ \
          -fsargs "-c c=64,a=16,e=16" -format UDRW -size ${size}k ${pack}
    
    
    # 3. Mount the disk image, and store the device name (you might want
    # to use sleep for a few seconds after this operation):
    
    device=$(hdiutil attach -readwrite -noverify -noautoopen "${pack}" | \
             egrep '^/dev/' | sed 1q | awk '{print $1}')
    
    
    # 4. Store the background picture (in PNG format) in a folder called
    # ".background" in the DMG, and store its name in the
    # "backgroundPictureName" variable.
    
    ## TODO
    mkdir /Volumes/$finalDMGName/.background
    cp gfx_src/folder_bg.png /Volumes/$finalDMGName/.background/
    backgroundPictureName=folder_bg.png

    # 5. Use AppleScript to set the visual styles (name of .app must be in
    # bash variable "applicationName", use variables for the other
    # properties as needed):
    
    echo '
       tell application "Finder"
         tell disk "'${title}'"
               open
               set current view of container window to icon view
               set toolbar visible of container window to false
               set statusbar visible of container window to false
               set the bounds of container window to {400, 100, 885, 430}
               set theViewOptions to the icon view options of container window
               set arrangement of theViewOptions to not arranged
               set icon size of theViewOptions to 72
               set background picture of theViewOptions to file ".background:'${backgroundPictureName}'"
               make new alias file at container window to POSIX file "/Applications" with properties {name:"Applications"}
               set position of item "'${applicationName}'" of container window to {100, 100}
               set position of item "Applications" of container window to {375, 100}
               -- On Snow Leopard, the above applescript will not set the icon position correctly; this is the fix:
               close
               open
    
               update without registering applications
               delay 5
               -- eject
         end tell
       end tell
    ' | osascript
    
    
    # 6. Finialize the DMG by setting permissions properly, compressing
    # and releasing it:
    
    #echo
    #echo "You may now arrange icons inside the package window."
    #sudo -k chmod -Rf go-w /Volumes/"${title}"

    sudo -p "Sudo will now set needed permissions on volume. Please enter your password: " chmod -Rf go-w /Volumes/"${title}"
    sync
    sync
    hdiutil detach ${device}
    hdiutil convert "${pack}" -format UDZO -imagekey zlib-level=9 -o "${finalDMGName}"
    rm -f ${pack} 
}
    
###############################################################################

part1
part2

echo
echo "Done. See ${finalDMGName}.dmg"
