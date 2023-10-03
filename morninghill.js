let infoModal
function handleClick(id) {
    console.log("Clicked button with ID: " + id);
    var button = document.getElementById(id);
    infoModal = document.getElementById('info'+id)
    console.log(id)
    console.log(button)
    console.log(infoModal)
    infoModal.showModal();
}
function check() {
    infoModal.close()
}
function close_dialog() {
    infoModal.close()
}
// yes.addEventListener("click", function () {
//     infoModal.close();
// })
// close_div.addEventListener("click", function () {
//     infoModal.close();
// })

function addOption(list, text, value){
	var index=list.options.length;
	list.options[index]=new Option(text, value);
	list.selectedIndex=index;
}
