// const oddsAndEvens = [13, 3, 4, 10, 7, 2];

// const retorneArrayOrdenado = () => {
//   oddsAndEvens[0] = 2;
//   oddsAndEvens[1] = 3;
//   oddsAndEvens[2] = 4;
//   oddsAndEvens[3] = 7;
//   oddsAndEvens[4] = 10;
//   oddsAndEvens[5] = 13;

//   return oddsAndEvens;

// }

// const arrayOrdenado = retorneArrayOrdenado();
// console.log(`Os números ${arrayOrdenado} se encontram ordenados de forma crescente!`);


const oddsAndEvens = [13, 3, 4, 10, 7, 2];

const retorneArrayOrdenado2 = oddsAndEvens.sort((a, b) => a - b);


console.log(`Os números ${retorneArrayOrdenado2} se encontram ordenados de forma crescente!`);