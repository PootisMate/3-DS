/*1*/
let nomes = ['Joaquim', 'Rafael', 'Luiz', 'Tomas']

let nomesComMaisDeCincoLetras = [];
for (let i = 0; i < nomes.length; i++) {
  if (nomes[i].length > 5) {
    nomesComMaisDeCincoLetras.push(nomes[i]);
  }
}

console.log(nomesComMaisDeCincoLetras);
  
/*2*/
let numeros = [18, 25, 37, 47, 53];
let soma = 0;
for (let i = 0; i < numeros.length; i++) {
  soma += numeros[i];
}
let media = soma / numeros.length;
console.log("A média é:", media);

/*3*/
let dezena = true
let numero = 11
while(dezena==true){
  numero = numero - 1
  console.log(numero)
  if(numero ==1){
    dezena=false }}
    
/*4*/
let palavras = ["concreto", "prego", "bastardos", "ferramentas", "capacetes"];
let maiorPalavra = "";
for (let i = 0; i < palavras.length; i++) {
  if (palavras[i].length > maiorPalavra.length) {
    maiorPalavra = palavras[i];
  }
}
console.log("A maior palavra é:", maiorPalavra);