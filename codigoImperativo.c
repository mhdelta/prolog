#include <iostream>
#include <stdlib.h>
#include <unistd.h>

#define clear() printf("\033[H\033[J")

using namespace std;

void padeceMoko(){
	clear();
	printf("%s\n", "SU CULTIVO TIENE ALGUNO DE ESTOS SINTOMAS?");
	printf("\n\n%s\n", "Los hijos o rebrotes de plantas enfermas pueden quedar pequeños, retorcerse y ponerse negros.");
	printf("%s\n", "Se presenta un secamiento de los bordes de las hojas, seguido de una franja de color amarillo intenso.");
	printf("%s\n", "Se presentan racimos y dedos deformes, alguna fruta se madura antes de tiempo, además los dedos se rajan cuando el racimo está muy desarrollado.");

	printf("%s\n\n", "[1]. SI \t[2]. NO");

	int op;

	scanf("%d", &op);
	clear();
	if(op == 1){
		printf("%s\n", "Su cultivo de platano padece de Mokoo madurabiche (Ralstonia solanacearum E. F.)");
	}
	if(op == 2){
		printf("%s\n", "Su cultivo tiene una gran probabilidad de padecer Moko o madurabiche (Ralstonia solanacearum E. F.)");
	}
}

void padecePudricion(){
	clear();
	printf("%s\n","SU CULTIVO TIENE ALGUNO DE ESTOS SINTOMAS?");
	printf("\n\n%s\n","Manchas acuosas, translúcidas, de color amarillento en sus comienzos y rojizo a castaño oscuro en sus últimas instancias.");
	printf("%s\n", "Un olor repugnante de los tejidos afectados se percibe e internamente se llena de un líquido cristalino que emana abundantemente al hacer presión sobre dichos tejidos. ");
	printf("%s\n\n", "[1]. SI \t[2]. NO");

	int op;

	scanf("%d", &op);
	clear();
	if(op == 1){
		printf("%s\n", "Su cultivo padece de pudrición acuosa del pseudotallo o bacteriosis (Dickeya chrysanthemi)");
	}
	if(op == 2){
		printf("%s\n", "Su cultivo tiene una gran probabilidad de padecer pudrición acuosa del pseudotallo o bacteriosis (Dickeya chrysanthemi)");
	}
}
void padeceMalPanama(){
	clear();
	printf("%s\n","SU CULTIVO TIENE ALGUNO DE ESTOS SINTOMAS?");
	printf("\n\n%s\n","Amarillamiento de las hojas más adultas a lo largo del margen foliar que continúa hacia la nervadura central hasta quedar las hojas completamente marchitas y de color café;");
	printf("%s\n", "Decoloración vascular en el interior del pseudotallo; líneas de color marrón, rojo o amarillo");
	printf("%s\n", "estrías necróticas, oscuras o azuladas pueden observarse sobre un fondo blanco");
	printf("%s\n", "manchas de color marrón o rojizos en el borde de la bráctea o de color oscuro de variados tamaños y distribuidos en diferentes regiones de la inflorescencia.");
	printf("%s\n\n", "[1]. SI \t[2]. NO");

	int op;

	scanf("%d", &op);
	clear();
	if(op == 1){
		printf("%s\n", "Su cultivo padece de pudrición acuosa del pseudotallo o bacteriosis (Dickeya chrysanthemi)");
	}
	if(op == 2){
		printf("%s\n", "Su cultivo tiene una gran probabilidad de padecer pudrición acuosa del pseudotallo o bacteriosis (Dickeya chrysanthemi)");
	}
}
void sigatokaNegra(){
	clear();
	printf("%s\n","SU CULTIVO TIENE ALGUNO DE ESTOS SINTOMAS?");
	printf("\n\n%s\n","En las plantas adultas, se presenta un gran número de rayas y manchas de color café a negro, son más notorias por debajo de las hojas");
	printf("%s\n", "Manchas con el centro hundido, de color gris, rodeados por un anillo negro, bien definido y un halo amarillo brillante, a simple vista se pueden observar los peritecios.  Las manchas son visibles en hojas secas porque el anillo persiste");
	printf("%s\n", "Estrías necróticas, oscuras o azuladas pueden observarse sobre un fondo blanco");
	printf("%s\n", "Manchas negras rodeadas a veces de un halo amarillento y centro ligeramente hundido");
	printf("%s\n\n", "[1]. SI \t[2]. NO");

	int op;

	scanf("%d", &op);
	clear();
	if(op == 1){
		printf("%s\n", "Su cultivo padece de pudrición acuosa del pseudotallo o bacteriosis (Dickeya chrysanthemi)");
	}
	if(op == 2){
		printf("%s\n", "Su cultivo tiene una gran probabilidad de padecer pudrición acuosa del pseudotallo o bacteriosis (Dickeya chrysanthemi)");
	}
}
void selector_enfermedad(int a, int b, int c, int d){
	if(a){
		padeceMoko();
		sleep(3);
	}
	if(b){
		padecePudricion();
	}
	if(c){
		padeceMalPanama();
	}
	if(d){
		sigatokaNegra();
	}


}
void sintomas_1(){
	printf("%s\n","\n[1]. Se presentan marchitamientos y amarilleamiento de plantas, las hojas se secan y se quiebran, pero sin desprenderse de la planta."); // primera enfermedad 
	printf("%s\n","\n[2]. Se observa inicialmente una quemazón en el borde de las hojas más viejas que luego avanza a toda la lámina foliar, ocasionando un amarillamiento total de la hoja."); //segunda enf..	
	printf("%s\n","\n[3]. Marchitez , pudrición en semillas, pudrición de raíces, tallos, cormos y tubérculos.");	//Tercer enfer..
	printf("%s\n","\n[4]. Manchas necróticas de forma elíptica, de color café en el envés y negro en el haz."); //..
}
int main(){
	char m, p;
	int x;
	int a = 0, b= 0, c= 0, d= 0;
	while(1){
			printf("%s\n", "[A] Seleccione un sintoma, [B] Verificar enfermedad");
			m=getchar();
	    	getchar();
		switch(m){
	    	case 'A': 
	    		sintomas_1(); 
	    		p = getchar();
	    		getchar();
	    		switch(p){
	    			case '1': a=1; break;
	    			case '2': b=1; break;
	    			case '3': c=1; break;
	    			case '4': d=1; break;
	    		}
	    		clear();
	    		break;
	    	case 'B': selector_enfermedad(a,b,c,d);
	    	case 'S': exit(0);  
	    	default: puts("\nSaliendo del programa..."); exit(0);
		}
	}
}
