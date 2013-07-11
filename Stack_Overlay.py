import os
from javax.swing import JPanel, JComboBox, JLabel, JFrame, JScrollPane, JColorChooser, JButton, JSeparator, SwingConstants, SpinnerNumberModel, JSpinner, BorderFactory
from java.awt import Color, GridLayout
from ij import IJ, WindowManager
from java.lang import System
from net.miginfocom.swing import MigLayout

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


class StackOverlay:
    def __init__(self):
        self.frame = None
        self.overlayColorPreviewLabel = None
        self.showStackOverlayWindow()

    def onQuit(self, e):
        print "Exiting..."
        self.frame.dispose()
        
    def showColorChooser(self, e):
        colorChooser = JColorChooser()
        self.overlayColor = colorChooser.showDialog(self.frame, "Choose color", Color.red)
        self.overlayColorPreviewLabel.setBackground(self.overlayColor)

    def showStackOverlayWindow(self):
        all = JPanel()
        all.setLayout(MigLayout())

        self.imageIDs = WindowManager.getIDList()
        self.imageNames = []

        for i in self.imageIDs:
            self.imageNames.append(WindowManager.getImage(i).getTitle())

        baseImageBox = JComboBox(self.imageNames)
        baseImageBoxLabel = JLabel("Base image")
        baseImageBox.setSelectedIndex(0)
        all.add(baseImageBoxLabel)
        all.add(baseImageBox, "wrap")

        overlayImageBox = JComboBox(self.imageNames)
        overlayImageBoxLabel = JLabel("Overlay image")
        if len(self.imageNames) > 1:
            overlayImageBox.setSelectedIndex(1)

        all.add(overlayImageBoxLabel, "gap unrelated")
        all.add(overlayImageBox, "wrap")

        all.add(JSeparator(SwingConstants.HORIZONTAL), "span, wrap")

        overlayStyleFrame = JPanel()
        overlayStyleFrame.setLayout(MigLayout())

        colorLabel = JLabel("Overlay color")
        self.overlayColorPreviewLabel = JLabel("           ")
        self.overlayColorPreviewLabel.setBorder(BorderFactory.createEmptyBorder(0,0,1,0))
        self.overlayColorPreviewLabel.setOpaque(True)
        self.overlayColorPreviewLabel.setBackground(Color.red)
        colorPicker = JColorChooser()
        colorPicker.setPreviewPanel(self.overlayColorPreviewLabel)
        colorButton = JButton("Select color...", actionPerformed=self.showColorChooser)

        opacityLabel = JLabel("Overlay opacity (%)")
        opacitySpinnerModel = SpinnerNumberModel(100, 0, 100, 1)
        opacitySpinner = JSpinner(opacitySpinnerModel)

        overlayStyleFrame.add(colorLabel)
        overlayStyleFrame.add(self.overlayColorPreviewLabel)
        overlayStyleFrame.add(colorButton, "wrap")

        overlayStyleFrame.add(opacityLabel)
        overlayStyleFrame.add(opacitySpinner, "wrap")

        all.add(overlayStyleFrame, "span, wrap")

        # TODO: add non-thermonuclear cancel button functionality
        overlayCancelButton = JButton("Cancel", actionPerformed=self.onQuit)
        overlayStartButton = JButton("Overlay images")

        all.add(overlayCancelButton, "gapleft push")
        all.add(overlayStartButton, "gapleft push")

        self.frame = JFrame("Stack Overlay")
        self.frame.getContentPane().add(JScrollPane(all))
        self.frame.pack()
        self.frame.setLocationRelativeTo(None)
        self.frame.setVisible(True)

stackOverlay = StackOverlay()

print "Done."
