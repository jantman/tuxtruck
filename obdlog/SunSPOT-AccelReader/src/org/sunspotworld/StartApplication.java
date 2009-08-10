/*
 * StartApplication.java
 *
 * Created on Aug 10, 2009 3:55:14 PM;
 */

package org.sunspotworld;

import com.sun.spot.peripheral.Spot;
import com.sun.spot.sensorboard.EDemoBoard;
import com.sun.spot.sensorboard.peripheral.IAccelerometer3D;
import com.sun.spot.sensorboard.peripheral.ISwitch;
import com.sun.spot.sensorboard.peripheral.ITriColorLED;
import com.sun.spot.util.*;

import java.io.*;
import javax.microedition.io.*;
import javax.microedition.midlet.MIDlet;
import javax.microedition.midlet.MIDletStateChangeException;

/**
 * The startApp method of this class is called by the VM to start the
 * application.
 * 
 * The manifest specifies this class as MIDlet-1, which means it will
 * be selected for execution.
 */
public class StartApplication extends MIDlet {

    private ITriColorLED [] leds = EDemoBoard.getInstance().getLEDs();
    private IAccelerometer3D acc = EDemoBoard.getInstance().getAccelerometer();

    protected void startApp() throws MIDletStateChangeException {

        System.out.println("Starting AccelReader app...");

        ISwitch sw1 = EDemoBoard.getInstance().getSwitches()[EDemoBoard.SW1];

        double accel, accelX, accelY, accelZ, tiltX, tiltY, tiltZ;
        String s = "";

        leds[0].setRGB(100,0,0);                // set color to moderate red
        while (sw1.isOpen()) {                  // done when switch is pressed
            leds[0].setOn();                    // Blink LED
            try
            {
                accel = acc.getAccel();
                accelX = acc.getAccelX();
                accelY = acc.getAccelY();
                accelZ = acc.getAccelZ();
                tiltX = acc.getTiltX();
                tiltY = acc.getTiltY();
                tiltZ = acc.getTiltZ();
                s = Double.toString(accel) + "," + Double.toString(accelX) + "," + Double.toString(accelY) + "," + Double.toString(accelZ) + "," + Double.toString(tiltX) + "," + Double.toString(tiltY) + "," + Double.toString(tiltZ);
                System.out.println("Accel," + s);
            }
            catch(java.io.IOException ex)
            {
                System.out.println(ex.getMessage());
            }

            Utils.sleep(250);                   // wait 1/4 seconds
            leds[0].setOff();
            Utils.sleep(250);                  // wait 1 second
        }
        notifyDestroyed();                      // cause the MIDlet to exit
    }

    protected void pauseApp() {
        // This is not currently called by the Squawk VM
    }

    /**
     * Called if the MIDlet is terminated by the system.
     * I.e. if startApp throws any exception other than MIDletStateChangeException,
     * if the isolate running the MIDlet is killed with Isolate.exit(), or
     * if VM.stopVM() is called.
     * 
     * It is not called if MIDlet.notifyDestroyed() was called.
     *
     * @param unconditional If true when this method is called, the MIDlet must
     *    cleanup and release all resources. If false the MIDlet may throw
     *    MIDletStateChangeException  to indicate it does not want to be destroyed
     *    at this time.
     */
    protected void destroyApp(boolean unconditional) throws MIDletStateChangeException {
        for (int i = 0; i < 8; i++) {
            leds[i].setOff();
        }
    }
}
