import os
from javax.swing import JPanel, JComboBox, JLabel, JFrame, JScrollPane, JColorChooser, JButton, JSeparator, SwingConstants, SpinnerNumberModel, JSpinner, BorderFactory, JCheckBox
from java.awt import Color, GridLayout
from ij import IJ, WindowManager, ImagePlus, ImageStack
from java.lang import System
from net.miginfocom.swing import MigLayout

def AWTColorToArray(color):
    return [color.getRed(), color.getGreen(), color.getBlue()]

class StackOverlay:
    def __init__(self):
        self.frame = None
        self.overlayColorPreviewLabel = None
        self.showStackOverlayWindow()
        self.overlayColor = None

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

        if self.imageIDs is None:
            IJ.error("No open images", "Stack Overlay requires at least one image to be already open.")
            return

        for i in self.imageIDs:
            self.imageNames.append(WindowManager.getImage(i).getTitle())

        self.baseImageBox = JComboBox(self.imageNames)
        baseImageBoxLabel = JLabel("Base image")
        self.baseImageBox.setSelectedIndex(0)
        all.add(baseImageBoxLabel)
        all.add(self.baseImageBox, "wrap")

        self.overlayImageBox = JComboBox(self.imageNames)
        overlayImageBoxLabel = JLabel("Overlay image")
        if len(self.imageNames) > 1:
            self.overlayImageBox.setSelectedIndex(1)

        all.add(overlayImageBoxLabel, "gap unrelated")
        all.add(self.overlayImageBox, "wrap")

        all.add(JSeparator(SwingConstants.HORIZONTAL), "span, wrap")

        overlayStyleFrame = JPanel()
        overlayStyleFrame.setLayout(MigLayout())
        overlayStyleFrame.setBorder(BorderFactory.createCompoundBorder(BorderFactory.createTitledBorder("Overlay Style"), BorderFactory.createEmptyBorder(5,5,5,5)))

        colorLabel = JLabel("Overlay color")
        self.overlayColorPreviewLabel = JLabel("           ")
        self.overlayColorPreviewLabel.setBorder(BorderFactory.createEmptyBorder(0,0,1,0))
        self.overlayColorPreviewLabel.setOpaque(True)
        self.overlayColorPreviewLabel.setBackground(Color.red)
        self.overlayColor = Color.red
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
        
        self.virtualStackCheckbox = JCheckBox("Use Virtual Stack", True)
        all.add(self.virtualStackCheckbox, "span, wrap")

        # TODO: add non-thermonuclear cancel button functionality
        overlayCancelButton = JButton("Cancel", actionPerformed=self.onQuit)
        overlayStartButton = JButton("Overlay images", actionPerformed=self.overlayImages)
        
        all.add(overlayCancelButton, "gapleft push")
        all.add(overlayStartButton, "gapleft push")

        self.frame = JFrame("Stack Overlay")
        self.frame.getContentPane().add(JScrollPane(all))
        self.frame.pack()
        self.frame.setLocationRelativeTo(None)
        self.frame.setVisible(True)
        
    def overlayImages(self, e):
        impBase = WindowManager.getImage(self.imageIDs[self.baseImageBox.getSelectedIndex()])
        refBase = impBase.getStack().getProcessor(1)
        
        stack = ImageStack(refBase.width, refBase.height)
        
        for i in range(1, impBase.getStackSize()):
            base = impBase.getStack().getProcessor(i).convertToRGB()
            overlay = impBase.getStack().getProcessor(i).convertToRGB().getPixels()
            #overlayColored = map(lambda x: x * AWTColorToArray(self.overlayColor), overlay)
            IJ.showProgress(i, impBase.getStackSize())
            print 'slice %i of %i' %(i, impBase.getStackSize()) 
            stack.addSlice(impBase.getStack().getSliceLabel(i), base)
            
        ImagePlus("Stack Overlay from " + self.imageNames[self.baseImageBox.getSelectedIndex()] + " and " + self.imageNames[self.baseImageBox.getSelectedIndex()], stack).show()

class OverlayVirtualStack(VirtualStack):
    def __init__(self):
        self.last = None

    def getProcessor(self, i):
        pass

    def getSize(self):
        pass

    def getSliceLabel(self, i):
        pass

    def getWidth(self):
        pass

    def getHeight(self):
        pass

    def getPixels(self, i):
        return self.getProcessor(i).getPixels()
    def setPixels(self, i):
        pass

stackOverlay = StackOverlay()

print "Done."
