#include <ArduinoMotorCarrier.h>



//Variable to change the motor speed and direction
int duty = 25;


void setup()
{


  controller.begin();

  // Reboot the motor controller; brings every value back to default

  controller.reboot();
  delay(500);

  M1.setDuty(0);
  M2.setDuty(0);
  M3.setDuty(0);
  M4.setDuty(0);


}

void loop() {

  


    M1.setDuty(0);
    M2.setDuty(0);
    M3.setDuty(0);
    M4.setDuty(0);

    delay(3000);
 

    M1.setDuty(duty);
    M2.setDuty(-duty);
    M3.setDuty(duty);
    M4.setDuty(duty); 

    delay(2000);

    M1.setDuty(0);
    M2.setDuty(0);
    M3.setDuty(0);
    M4.setDuty(0);

    delay(500);
    
    M1.setDuty(duty);
    M2.setDuty(duty);
    M3.setDuty(duty);
    M4.setDuty(-duty);

    delay(2000);

    M1.setDuty(0);
    M2.setDuty(0);
    M3.setDuty(0);
    M4.setDuty(0);

    delay(500);

    M1.setDuty(duty);
    M2.setDuty(duty);
    M3.setDuty(-duty);
    M4.setDuty(duty);

    delay(2000);

    M1.setDuty(0);
    M2.setDuty(0);
    M3.setDuty(0);
    M4.setDuty(0);

    delay(500);

    M1.setDuty(-duty);
    M2.setDuty(-duty);
    M3.setDuty(duty);
    M4.setDuty(-duty);

    delay(2000);

    M1.setDuty(0);
    M2.setDuty(0);
    M3.setDuty(0);
    M4.setDuty(0);

    delay(5000);
  }
