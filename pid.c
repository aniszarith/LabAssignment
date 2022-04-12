#include <stdlib.h> /*to define exit()*/
#include <unistd.h> /*to define fork() and getpid()*/
#include <stdio.h> /*to define printf()*/
#include <sys/wait.h> 
int main(int argc, char **argv){
int pid; /*process ID*/
switch (pid = fork())
{ case 0: /*a forkm return 0 to the child*/
  printf ("I am the child process : pid=%d\n", getpid());
  break ;

  default:/*a fork returm a pid to the parent*/
  wait (NULL);
  printf ("I am the parent process : pid=%d, child pid=%d\n", getpid(), pid);
  break; 

  case -1:/*something wrong */
  perror("fork");
  exit(1);
}
exit(0);
}
