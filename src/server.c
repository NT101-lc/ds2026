#include <stdio.h>
#include <sys/socket.h>
#include <string.h>
#include <netinet/in.h>
#define PORT 8080


int main(){ 
  int server = socket(AF_INET, SOCK_STREAM, 0);

  struct sockaddr_in addr = {0};
  addr.sin_family = AF_INET;
  addr.sin_port = htons(8080);
  addr.sin_addr.s_addr = INADDR_ANY;
  
  bind(server, (struct sockaddr*)&addr, sizeof(addr));
  listen(server, 5);

  printf("Listening on port 8080 at the moment\n");
  accept(server, NULL, NULL);

  return 0;

}
