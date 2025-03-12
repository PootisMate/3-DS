let sede = true
let copos = 0
while(sede==true){
  copos=copos+1
  console.log("Bebendo copo de água:", copos)
  if(copos ==3){
    sede=false
  } 
}

let fome = true
let pedaços = 0
do{
  pedaços = pedaços + 1
  console.log("Comendo pedaço de bolo:", pedaços)
  if(pedaços>0){
    fome = false
  }
}while(fome==true)

/*1*/
let nome = ['Joaquim', 'Rafael', 'Luiz', 'Tomas']
let maior = ''
for(let ini=0;ini<nome.length;ini++){
  if (nome[ini].length>maior){
    maior = nome[ini]
  }
}
  console.log(nome)
  
/*2*/
let nota = [3,9,6]
let ni = []
for(let nota of notas)
  let media = (nota / nota.length)
console.log('Sua média é', media)

/*3*/
let dezena = true
let numero = 11
while(dezena==true){
  numero = numero - 1
  console.log(numero)
  if(numero ==1){
    dezena=false }}
    