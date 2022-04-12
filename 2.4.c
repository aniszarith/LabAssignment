#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void childTask() {
 char name[20];
 scanf("%s",name);
 printf ("My name is %s\n",name);
}

void parentTask() {
 printf ("Job is done\n");
}

int main(void){

 for (int i=0; i<4;i++){
  pid_t pid = fork();

  if (pid == 0)
  { printf ("What is your name? ");
   childTask();
   exit(0);
  }
  else
  { wait(NULL); }
  if (i == 3){parentTask();}
 }
return EXIT_SUCCESS ;
}
