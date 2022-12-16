#include <openssl/md5.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Compute MD5 of string argument. Length of string must be less than 512.
// Caller takes ownership of result.
char *md5(const char *str, int length) {
  char *ret = (char *)malloc(33);
  unsigned char digest[16];

  MD5((const unsigned char *)str, length, digest);
  for (int i = 0; i < 16; i++) {
    sprintf(ret + (i * 2), "%02x", (unsigned char)digest[i]);
  }

  return ret;
}

// Main
int main(int argc, char **argv) {
  char *name = "Marion Lang";
  char *sig = md5(name, strlen(name));

  printf("Hello %s! - %s\n", name, sig);

  printf("Writing to output file...");

  FILE *f = fopen("output.txt", "w");
  fprintf(f, "%s\n", sig);
  fclose(f);

  printf("Done!\n");

  free(sig);

  return 0;
}
