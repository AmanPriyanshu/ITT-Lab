function updateStatus(){
    var text = document.getElementById("inputText").value;
    var tokens = text.split(' ')
    var area_code = tokens[0];
    var tokens2 = tokens[1].split('-');
    var exchange = tokens2[0];
    var number = tokens2[1];
    var d1 = document.getElementById("output");
    document.getElementById("area_code").value = area_code;
	document.getElementById("exchange").value = exchange;
	document.getElementById("number").value = number;
	console.log(d1.innerHTML);
}