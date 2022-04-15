#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <signal.h>
#include <errno.h> 

void signal_handler(int sig){
  printf ("Excuse me\n");
 }

int main(void) {
  int fd[2];
  pipe(fd);
  pid_t pid = fork();
  void signal_handler(int sig);

 if(signal(SIGINT, signal_handler) == SIG_ERR){
   perror("signal");
   exit(1);
  }

  if(pid > 0) {//parent
    close(0); //close standard input
    close(fd[1]);//close write fd - no use in parent

    int adnum = 0;
    int okay = read(fd[0],&adnum, 1); //read 

    wait(NULL);
    printf("Number: %d\n",adnum);

     close (fd[0]);// close read fd after reading

     int flag = 0;

     if (adnum == 0||adnum == 1)
      { printf("Number %d is a prime number\n",adnum);}

     else {
     for (int i=2; i<=adnum/2; i++) {
          if (adnum % i == 0)
             {flag = 1; break;}
          }

     if (flag == 1){ printf("Number %d is not a prime number\n",adnum);}
     else if ( flag == 0) {printf ("Number %d is a prime number\n",adnum);}
    }
  }
  else if(pid == 0) {//child
    int chnum;
    printf ("Enter a number :");
    scanf ("%d",&chnum);
    close(1);//close standard input
    close(fd[0]);//close read fd - no use in child

    write(fd[1], &chnum, 1);//child write
    exit(EXIT_SUCCESS);
  }
  return EXIT_SUCCESS;
}
