import os
from javax.swing import JPanel, JComboBox, JLabel, JFrame, JScrollPane, JColorChooser, JButton, JSeparator, SwingConstants, SpinnerNumberModel, JSpinner
from java.awt import Color, GridLayout
from ij import IJ, WindowManager
from java.lang import System

from net.miginfocom.swing import MigLayout

def onQuit(e):
    print "Exiting..."

all = JPanel()
all.setLayout(MigLayout())

colorToRGB = {
'Red' : [255,0,0],
'Green' : [0,255,0],
'Blue' : [0,0,255],
'Orange' : [255,127,0],
'Cyan' : [0,255,255],
'Yellow' : [255,255,0],
'Magenta' : [255,0,255],
'Indigo' : [75,0,130],
'Violet' : [238,130,238],
'Greyscale' : [255,255,255],
'Aquamarine' : [127,255,212],
'Navy Blue' : [0,0,128],
'Sky Blye' : [135,206,235],
'Turquoise' : [64,224,208],
'Beige' : [245,245,220],
'Brown' : [165,42,42],
'Chocolate' : [210,105,30],
'Dark wood' : [133,94,66],
'Light wood' : [133,99,99],
'Olive' : [128,128,0],
'Green yellow' : [173,255,47],
'Sea green' : [32,178,170],
'Khaki' : [240,230,140],
'Salmon' : [250,128,114],
'Pink' : [255,192,203],
'Tomato' : [255,99,71],
'Scarlet' : [140,23,23],
'Purple' : [128,0,128],
'Wheat' : [245,222,179],
'Silver grey' : [192,192,192]
}

colors = ['Red', 'Green', 'Blue',
          'Orange', 'Indigo',
          'Cyan', 'Yellow', 'Magenta',
          'Turquoise', 'Tomato', 'Olive',
          'Violet', 'Green yellow', 'Khaki',
          'Scarlet', 'Beige', 'Chocolate',
          'Silver grey', 'Pink', 'Wheat',
          'Sea green', 'Greyscale', 'Light wood',
          'Sky Blye', 'Brown', 'Salmon', 'Navy Blue',
          'Aquamarine', 'Purple', 'Dark wood']

ids = WindowManager.getIDList()
names = []

for i in ids:
    names.append(WindowManager.getImage(i).getTitle())
    
baseImageBox = JComboBox(names)
baseImageBoxLabel = JLabel("Base image")
baseImageBox.setSelectedIndex(0)
all.add(baseImageBoxLabel)
all.add(baseImageBox)

overlayImageBox = JComboBox(names)
overlayImageBoxLabel = JLabel("Overlay image")
if len(names) > 1:
    overlayImageBox.setSelectedIndex(1)

all.add(overlayImageBoxLabel, "gap unrelated")
all.add(overlayImageBox, "wrap")

all.add(JSeparator(SwingConstants.HORIZONTAL), "span, wrap")

overlayStyleFrame = JPanel()
overlayStyleFrame.setLayout(MigLayout())
        
colorLabel = JLabel("Overlay color")
colorPicker = JColorChooser()

opacityLabel = JLabel("Overlay opacity (%)")
opacitySpinnerModel = SpinnerNumberModel(100, 0, 100, 1)
opacitySpinner = JSpinner(opacitySpinnerModel)

overlayStyleFrame.add(colorLabel)
overlayStyleFrame.add(colorPicker, "wrap")

overlayStyleFrame.add(opacityLabel)
overlayStyleFrame.add(opacitySpinner, "wrap")

all.add(overlayStyleFrame, "span, wrap")

# TODO: add non-thermonuclear cancel button functionality
overlayCancelButton = JButton("Cancel", actionPerformed=onQuit)
overlayStartButton = JButton("Overlay images")

all.add(overlayCancelButton, "gapleft push")
all.add(overlayStartButton, "gapleft push")

frame = JFrame("Stack Overlay")
frame.getContentPane().add(JScrollPane(all))
frame.pack()
frame.setLocationRelativeTo(None)
frame.setVisible(True)

IJ.showStatus("Hello, world!")
