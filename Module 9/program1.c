#include <stdio.h>
#include <math.h>

int main()
{
float length, width, perimeter, area, diagonal;
char choice;
int k = 1;
printf(" Enter the length: ");
scanf("%f", &length);
printf(" Enter the width: ");
scanf("%f", &width);

printf("\n Menu:");
printf("\n a. perimeter");
printf("\n b. area");
printf("\n c. diagonal");
printf("\n d. exit");

do
{

	printf("\n\n Choose your letter: ");
	scanf("%s", &choice);

if (choice == 'a')
{
	perimeter = 2*(length + width);
	printf(" The perimeter is: %.3f", perimeter);
	k++;
}

else if (choice == 'b')

{
	area =  length*width;
	printf(" The area is: %.3f", area);
	k++;
}

else if (choice ==  'c')
{
	diagonal = sqrt(length*length + width*width);
	printf(" The length of the diagonal is: %.3f", diagonal);
	k++;
}

else if (choice == 'd')
{
	printf(" Have a nice day!");
	return 0;
}
else 
{
	k++;
}

}while(k<=10);

	printf("\n You have exceeded the maximum number of invalid inputs. \n Have a nice day!");

return 0;
}

