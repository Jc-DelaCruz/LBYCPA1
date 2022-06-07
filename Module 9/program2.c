#include <stdio.h>
#include <math.h>
#include<stdlib.h>
 main()
{
	int count;
	float len, wid, peri,area,dia;
	char choice;
	count=1;
	
	printf("Enter the length: ");
	scanf("%f", &len);
	printf("\nEnter the width: ");
	scanf("%f", &wid);
	
	printf("\n\nMENU:");
	printf("\na. Perimeter");
	printf("\nb. Area");
	printf("\nc. Diagonal");
	printf("\nd. Exit");
	printf("\n\nChoose your letter: ");
	scanf("%s", &choice);
	
	do 
	{
	
		

		if(choice == 'a')
		{
			peri = 2 * (len + wid);
			printf("\nThe perimeter is %.3f", peri);
			printf("\n\nChoose your letter: ");
			scanf("%s", &choice);
		
		}
		else if(choice == 'b')
		{
			area = (len * wid);
			printf("\nThe area is %.3f", area);
			printf("\n\nChoose your letter: ");
			scanf("%s", &choice);
		
		}
		else if(choice == 'c')
		{
			dia = sqrt((pow(wid,2)) + (pow(len,2)));
			printf("\nThe diagonal is %.3f", dia);
			printf("\n\nChoose your letter: ");
			scanf("%s", &choice);
		
		}
		else if(choice == 'd')
		{
				printf("\nHave a nice day!");
				return 0;
		}
		
		else
		{
			printf("\nInvalid Input.");
			printf("\n\nChoose your letter: ");
			scanf("%s", &choice);
		}
		++count;
			
	}while (count <10);
	
		printf("\nYou have exceeded the maximum number of invalid inputs. \nHave a nice day!");
	
	
				
	
	
	
	return 0;
}
