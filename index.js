/*1*/

function operacao(a, b, callback){
  callback(a, b)
}

function soma(a, b){
  console.log("A soma é: ", a+b)
}
function subtracao(a, b){
  console.log("A subtração é: ", a-b)
}
function multiplicacao(a, b){
  console.log("A multiplicação é: ", a*b)
}
function divisao(a, b){
  console.log("A divisão é: ", a/b)
}
operacao(15, 30, soma)
operacao(15, 30, subtracao)
operacao(15, 30, multiplicacao)
operacao(15, 30, divisao)

/*2*/

let programas = ["Javascript", "Python", "C++"]

programas.forEach(elemento =>{
  console.log("Eu gosto de ", elemento)
})

/*3*/

let numeros = [5, 10, 15, 20]

numeros.forEach(Element =>{
  console.log(5+10+15+20)
})

/*4*/

let idades = [10, 15, 18, 21, 25]
let maiorDeIdade = idades.map(ano=>ano>=18)
console.log(maiorDeIdade)

/*5*/
let celsius = [0, 20, 30, 40]
let farenheit = celsius.map(temp => temp*1,8+32)
console.log(farenheit)
/*6*/

let precos = [100, 200, 300]
let desconto = precos.map(preco => preco*0.1)
console.log(desconto)