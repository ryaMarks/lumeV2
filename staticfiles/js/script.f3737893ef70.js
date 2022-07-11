
/** Dados gerais da obra */
var nome = ""; /* variavel que guarda o nome do cliente*/ 
var tel = ""; /*variavel que guarda o telefone do cliente*/
var end = ""; /* variavel que guarda o endereço do cliente*/ 
var eqLider = ""; /* variavel que guarda o nome do lider da equipe*/ 
var entrega = ""; /* variavel que guarda a data de entrega da obra*/ 

/**Dados do sistema */
var pot = "";
var inv = "";
var nInv = "";
var mod = "";
var nMod = "";
var strBx = "";
var padrao = "";
var observacao = "";


function getVal () {  /*função que pega os dados cadastrados e exibe na pagina web */
    
    /**Pega os dados gerais da obra */
    nome = document.getElementById('nome').value; /* Guarda o nome inserido*/
    tel = document.getElementById('telefone').value;/* Guarda o telefone inserido*/
    end = document.getElementById('endereco').value;/*Guarda o endereço inserido*/
    eqLider = document.getElementById('equipe').value;/*Guarda o nome inserido*/
    entrega = document.getElementById('date').value;/*Guarda  data inserida*/

    /**Pega os dados do sistema */
    pot = document.getElementById('potSis').value;
    inv = document.getElementById('inv').value;
    nInv = document.getElementById('nInv').value;
    mod = document.getElementById('mod').value;
    nMod = document.getElementById('nMod').value;
    strBx = document.getElementById('strBx').value;
    padrao= document.getElementById('padrao').value;
    observacao = document.getElementById('obs').value;
    
    /* Envia a string de saida de acordo com as entradas */
    if ((nome == "")||(tel == "")||(end == "")||(eqLider == "")||(entrega == "")){ /* Se o nome ou o email forem vazios */
        alert("Insira os dados corretamente");  /*informa mensagem de alerta */
    }else{/* Se os dados inseridos não forem vazios */
        console.log(nome + tel);
    }

}
