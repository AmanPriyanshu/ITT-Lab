function updateStatus(){
    var text = document.getElementById("inputText").value;
    var tokens = text.split(' ')
    var area_code = tokens[0];
    var tokens2 = tokens[1].split('-');
    var exchange = tokens2[0];
    var number = tokens2[1];
    var d1 = document.getElementById("output");
    d1.insertAdjacentHTML('afterbegin', '<p> area_code:' + area_code + '</br> exchange: '+exchange+'</br> number: '+number+' </p>');
    console.log(d1.innerHTML);
}