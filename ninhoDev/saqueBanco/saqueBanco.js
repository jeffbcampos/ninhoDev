let nota100 = 0;
let nota50 = 0;
let nota20 = 0;
let nota10 = 0;
let nota5 = 0;
let nota2 = 0;
let nota1 = 0;
let saque = 0;

let saldo = parseFloat(prompt("Digite a quantidade do seu Saldo:"));

saque = parseFloat(prompt(`Seu saldo é R$ ${saldo}\n\nDigite o valor que deseja sacar`));

let quantiaSaque = saque;

if (saque > saldo) {
    quantiaSaque = 0;
    alert("Saldo insuficiente para saque! Encerrando programa...")
} else {
    while(saque != 0) {
        if (saque >= 100) {
            nota100++;            
            saque -= 100;
            saldo -= 100;            
        } else if(saque >= 50) {
            nota50++;
            saque -= 50;
            saldo -= 50;
        } else if(saque >= 20) {
            nota20++;
            saque -= 20;
            saldo -= 20;
        } else if(saque >= 10) {
            nota10++;
            saque -= 10;
            saldo -= 10;
        } else if(saque >= 5) {
            nota5++;
            saque -= 5;
            saldo -= 5;
        } else if(saque >= 2) {
            nota2++;
            saque -= 2;
            saldo -= 2;
        } else if(saque >= 1) {
            nota1++;
            saque -= 1;
            saldo -= 1;
        }
    }
}

alert(`Você sacou R$ ${quantiaSaque}\n\nSeu saldo restante é R$ ${saldo}\n\nVoce sacou:\n${nota100} notas de 100\n${nota50} notas de 50\n${nota20} notas de 20\n${nota10} notas de 10\n${nota5} notas de 5\n${nota2} notas de 2\n${nota1} notas de 1`)

// teste