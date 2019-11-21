#include <iostream>
#include <cstdio>
using namespace std;
int main(){
	FILE *f = fopen("mkdir.bat","wb+");
	fprintf(f, "md ");
	for (int i=121; i<240; i++){
		fprintf(f,"%d,",i);
	}	
	fprintf(f,"240");
	fclose(f);
}
