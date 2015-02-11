Anamorphy
(C) by Pascal Bauermeister, September 2013.
Version @CURRENT_VERSION@, built on %%mtime(%Y-%m-%d).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Please edit this file to change README.html, which is auto-generated using
% the txt2tags utility (see http://txt2tags.org/) at build-time.
%
% Please respect the txt2tags syntax (http://txt2tags.org/markup.html) in the
% current file.
%
% ATTENTION: please be sure to leave TWO blank lines after lists!
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

= Purpose =

Thank you for using Anamorphy.

Anamorphy is an interactive program to create anamorphosis images.

An anamorphosis is a drawing mapped on a surface, and
sheared in such a way that, when seen from a well-defined
location, it appears as not deformed, but floating in front of
the surface.  For more information look for 'Anamorphosis'
on Wikipedia.

Outputs of this program can be printed as simple or folded
cards, or can be used to paint anamorphosis on buildings,
boxes or on the floor.

This program dedicated to the [Instructables www.instructables.com]
community.


= License =

Anamorphy is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.

Anamorphy is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details. You should have received a
copy of the GNU General Public License along with Anamorphy; if not,
write to the Free Software Foundation, Inc., 59 Temple Place, Suite
330, Boston, MA 02111-1307 USA

= History =

Version @CURRENT_VERSION@:
- Initial release


= How to Get the Sources =

...


= Credits and Copyright =

(C) copyright 2013 by P. Bauermeister.


== Third-party software with portions embedded into the run-time ==

: Python 2.7
- An interpreted, general-purpose high-level programming language whose design
  philosophy emphasizes code readability. Python aims to combine "remarkable
  power with very clear syntax", and its standard library is large and
  comprehensive. Its use of indentation for block delimiters is unusual among
  popular programming languages.

  Python supports multiple programming paradigms, primarily but not limited to
  object oriented, imperative and, to a lesser extent, functional programming
  styles. It features a fully dynamic type system and automatic memory
  management, similar to that of Scheme, Ruby, Perl, and Tcl. Like other
  dynamic languages, Python is often used as a scripting language, but is also
  used in a wide range of non-scripting contexts.
- Home:     http://www.python.org/
- Download: http://www.python.org/download/
- Usage:    The application is written in Python.


: wxPython2.8
- wxPython is a wrapper for the cross-platform GUI API (often referred
  to as a 'toolkit') wxWidgets (which is written in C++) for the
  Python programming language. It is one of the alternatives to
  Tkinter, which is bundled with Python. It is implemented as a Python
  extension module (native code). Other popular alternatives are PyGTK
  and PyQt. Like wxWidgets, wxPython is free software.
- Home:     http://wxpython.org/
- Download: http://wxpython.org/download.php#stable
- Usage:    The application's GUI is made with wxPython.


== Third-party software used at build-time ==

: Inno Setup with InnoIDE 5.4.
- Inno Setup is a free script-driven installation system created in
  CodeGear Delphi by Jordan Russell.
- Home:     http://www.InnoIDE.org and http://www.jrsoftware.org/isinfo.php
- Download: http://www.innoide.org/download.php
- Usage:    The setup EXE is built using InnoIDE.


: py2exe-0.6.9
- py2exe is a Python extension which converts Python scripts (.py)
  into Windows executables (.exe). These executables can run on a
  system without Python installed.
- Home:     http://www.py2exe.org/
- Download: http://sourceforge.net/projects/py2exe/files/
- Usage:    The application uses py2exe to make it independant from the
            Python interpreter.


: wxGlade 0.6.3
- wxGlade is a program for creating wxWidgets GUIs. It can generate layout code
  for C++, Python and Perl.
- Home:     http://wxglade.sourceforge.net/
- Download: http://sourceforge.net/projects/wxglade/
- Usage:    exGlade is used to design and maintain the GUI of the application.


: txt2tags-2.6
- txt2tags is a document generator software that uses a lightweight
  markup language. txt2tags is free software under GNU General Public
  License.

  Written in Python, it can export documents to several formats
  including: HTML, XHTML, SGML, LaTeX, Lout, roff, MediaWiki, Google
  Code Wiki, DokuWiki, MoinMoin, MagicPoint, PageMaker and plain text.
- Home:     http://txt2tags.org/
- Download: http://txt2tags.org/download.html
- Usage:    Script used at build-time to generate product README as HTML page.


= Q&A =

== Question: ZZZ ==
Answer: XXX

== Question: Why Python? ==
Answer: Python allows remarkably fast, concise, clean and efficient designs. It
comes with many built-in features (HTTP, XML, ZIP, etc), and is platform-
independent. Not least, the initial developer (Pascal) has extensive experience
with Python.

== Question: Why WxWidgets? ==
Answer: WxWidgets offers a large choice of widgets, controls, containers, and is
platform-independent. The GUI features are implemented, on a given platform,
with as many native features as possible. Hence, the look and feel is the one
of the platform (unlike e.g. Java Swing). The programming model is very clean
and easy to work with. Furthermore, it has a builder, wxGlade, giving fairly
good results.

== Question: Why does the installer take up 4.6 MB? ==
Answer: Because it contains some parts of the Python interpreter, and
some needed libraries (e.g. WxWidgets). In fact, it will take some
more space on disk once installed.


--------------------
``end of file``
