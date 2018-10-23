/*
This files make an executable file to execute the Python file, current_time.py
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

int minute(const char *);
void pause (float);

int main()
{
    //printf("Current time: %s\n", time_str);
    FILE * pin;
    int min, i;
    bool controle = false;
    while(1){
        time_t mytime = time(NULL);
        char * time_str = ctime(&mytime);
        time_str[strlen(time_str) - 1] = '\0';
        min = minute(time_str);
        printf(".");
        pause(60);
        pin = fopen("time.txt", "w");
        fputs(time_str, pin);
        fclose(pin);
        pin = fopen("time.txt", "r");
        system("python tweetar.py");
        fclose(pin);
    }
    //printf("Current minute: %d\n", min);
    return 0;
}

int minute(const char * str)
{
    char tempo[3];
    int val;
    strncpy(tempo, &str[14], 2);
    tempo[2] = '\0';
    val = atoi(tempo);
    return val;
}

void pause (float delay1) {

   if (delay1<0.001) return; // pode ser ajustado e/ou evita-se valores negativos.

   float inst1=0, inst2=0;

   inst1 = (float)clock()/(float)CLOCKS_PER_SEC;

   while (inst2-inst1<delay1) inst2 = (float)clock()/(float)CLOCKS_PER_SEC;

   return;

}
