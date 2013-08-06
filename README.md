Stack Overlay Plugin for Fiji
=============================

Overview
--------
With this plugin, you can create a colored overlay of two images.
This is especially useful when you want to check an images' segmentation
against the original version.

Installation
------------
For building the plugin, you need:

* Java Development Kit
* Fiji, http://fiji.sc - obviously ;)

After you've cloned the repository, simply run `./build.sh`. Copy the
resulting `Stack_Overlay.jar` to your Fiji plugins directory.
You'll find the plugin under `Plugins > Stack Overlay`.

Known issues
------------

* Launching the Stack Overlay plugin for the first time after you have
  started Fiji takes a bit of time as it has to load the Jython interpreter.
* not using a Virtual Stack is not implemented yet.
* overlay opacity is not implemented yet.


License
-------
Stack Overlay is licensed under the 2 clause BSD license. See LICENSE file for details.
The repository includes MigLayout, which is under the same license.
