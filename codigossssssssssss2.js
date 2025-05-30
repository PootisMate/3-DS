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

/*Exercícios de objetos*/

/*1*/
let aluno = {
  gênero : "masculino",
  nome : "Pootis de la Mate",
  série : "3°DS B"
};
console.log(aluno);

/*2*/

let carro = {
  marca: "BYD",
  modelo: "Dolphin",
  ano: 2015
};

carro.cor = "Preto";
carro.ano = 2018;

console.log(carro);

/*3*/

let produto = {
  nome: "Celular",
  preco: 1800,
  estoque: 25
};

delete produto.estoque;

console.log(produto);

/*4*/

let pessoa = {
  nome : "Konkey Dong",
  idade : 27,

  apresentar(){
    console.log(`Uhhuuhuuuhuuu, suu ${this.nome} e tenhu ${this.idade} anuus`);
  }
};

pessoa.apresentar();

/*5*/

let filme = {
  titulo: "Matrix",
  diretor: "Lana Wachowski",
  ano: 1999
};

for(let chave in filme){
  console.log(filme[chave]);
}

/*6*/

let turma = [
  { nome: "Carlinhos", idade: 10, nota: 5.2 },
  { nome: "Reboleca", idade: 37, nota: 3.0 },
  { nome: "LucasArcano.2009 enjoyer", idade: 26, nota: 9.2 }
];

turma.forEach(aluno => console.log(aluno.nota));

/*7*/

let contaBancária = {
  titular: "Spiff",
  saldo: 7000,
 
  depositar(valor){
    this.saldo += valor;
    console.log(`Depósito de R$${valor} realizado. Saldo atual: R$${this.saldo}`);
  },
 
  sacar(valor){
    if(valor > this.saldo){
      console.log("Saldo insuficiente.");
    } else {
      this.saldo -= valor;
      console.log(`Saque de R$${valor} realizado. Saldo atual: R$${this.saldo}`);
    }
  }
};

contaBancária.depositar(500);
contaBancária.sacar(200);
contaBancária.sacar(2000);
