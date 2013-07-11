import ij.*;
import ij.process.*;
import ij.gui.*;
import java.awt.*;
import ij.plugin.*;
import ij.plugin.frame.*;
import ij.gui.GenericDialog;
import ij.gui.DialogListener;

import java.awt.AWTEvent;
import java.awt.Button;
import java.awt.Checkbox;
import java.awt.Choice;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.Insets;
import java.awt.Label;
import java.awt.Panel;
import java.awt.Point;
import java.awt.Rectangle;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.TimeZone;

public class TransparentStackOverlay implements PlugIn {

	@SuppressWarnings("serial")
	protected class OverlayPropertiesPanel extends Panel{
		/**
		 * Creates a new {@link FontPropertiesPanel} containing the font setting
		 * and font colour buttons.
		 */
		public OverlayPropertiesPanel() {
			super(null);

			Button fontColourButton = new Button("Font Color");
			fontColourButton.setBounds(130, 0, 120, 25);
			fontColourButton.addActionListener(new ActionListener() {
				public void actionPerformed(ActionEvent actionEvent) {
					new ColorPicker();

				}
			});

			add(fontColourButton);
		}
	}

	public void run(String arg) {
		ImagePlus original = WindowManager.getCurrentImage();
		if (original == null) {
			IJ.error("At least one image has to be open.");
			return;
		}

		GenericDialog gd = new NonBlockingGenericDialog("Transparent Stack Overlay");
		String[] images = {"blubb", "bla"};
		gd.addChoice("Base image stack", images, "bla");
		gd.addChoice("Overlay image stack", images, "bla");

		OverlayPropertiesPanel propertiesPanel = new OverlayPropertiesPanel();
		propertiesPanel.setBounds(10, 70, 400, 50);
		
		gd.addPanel(propertiesPanel);

		IJ.addEventListener(new IJEventListener() {
			public void eventOccurred(int event) {
				if (event == IJEventListener.FOREGROUND_COLOR_CHANGED
						|| event == IJEventListener.BACKGROUND_COLOR_CHANGED) {
					//updatePreview();
				}
			}
		});

		gd.showDialog();
		if( gd.wasCanceled() )
			return;

		
	}

}
