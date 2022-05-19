#include<stdio.h>
#include<string.h>      //strlen
#include<sys/socket.h>
#include<arpa/inet.h>   //inet_addr
#include<unistd.h>      //write
#include <netinet/in.h>
#include <sys/types.h>
#include <stdlib.h>
#include <netdb.h>
#define MAX 2000
#define PORT 8888

void func(int new_socket)
{
   char buff[MAX];
   int n;

   for(;;) {
     bzero(buff,MAX);
    read (new_socket, buff, sizeof(buff));

    printf("Client : %s\t Server: ", buff);
    bzero(buff, MAX);
    n=0;

    while((buff[n++] = getchar()) != '\n')
    ;
    write(new_socket, buff, sizeof(buff));
    if(strncmp("exit",buff,4) == 0)
    { printf("Server exit..\n");
      break;
    }
  }
}

int main(int argc , char *argv[])
{
        int socket_desc , new_socket , c;
        struct sockaddr_in server , client;

        //Create socket
        socket_desc = socket(AF_INET , SOCK_STREAM , 0);
        if (socket_desc == -1)
        {
                printf("Could not create socket");
        }

        //Prepare the sockaddr_in structure
        server.sin_family = AF_INET;
        server.sin_addr.s_addr = INADDR_ANY;
        server.sin_port = htons( 8888 );
        //Bind
        if( bind(socket_desc,(struct sockaddr *)&server , sizeof(server)) < 0)
        {
                puts("bind failed");
                return 1;
        }
        puts("bind done");

        //Listen
        listen(socket_desc , 3);

        //Accept and incoming connection
        puts("Waiting for incoming connections...");
        c = sizeof(client);

        new_socket = accept(socket_desc, (struct sockaddr *)&client,&c);

        if (new_socket<0)
        {
                perror("accept failed");
                return 1;
        }
        else  puts("RECEIVED");

        func(new_socket);
        close(socket_desc);
        return 0;
}
