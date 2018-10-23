#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int minute(const char *);

int main()
{
    //printf("Current time: %s\n", time_str);
    FILE * pin;

    while(1){
        int min;
        time_t mytime = time(NULL);
        char * time_str = ctime(&mytime);
        time_str[strlen(time_str) - 1] = '\0';
        min = minute(time_str);
        printf(".");
        if(min % 15 == 0){
            pin = fopen("time.txt", "w");
            fputs(time_str, pin);
            fclose(pin);
            pin = fopen("time.txt", "r");
            system("python tweetar.py");
            fclose(pin);
        }
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
