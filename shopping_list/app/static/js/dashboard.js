function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
		
	document.getElementById('id01').style.display = "none";
    document.getElementById(tabName).style.display = "block";
    //evt.currentTarget.className += " active";
	
}

function getListName(event){
	var listName = document.getElementById('shoppinglist').value;
    document.getElementById("listhdr").innerHTML = "<h3>New Shopping List - " + listName + "</h3>";
    document.getElementById("listname").value = listName;
    //alert(document.getElementById("listname").value);
	openTab(event, 'NewList');
	
}

function addRowNewList() {
	var numberOfRows = document.getElementById("newListTable").rows.length;
    var table = document.getElementById("newListTable");
    var row = table.insertRow(numberOfRows);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
	var cell3 = row.insertCell(2);
	
    cell1.innerHTML = "<input style='width:100%' name='itemdescription" + (numberOfRows-1) + "' required/>";
    cell2.innerHTML = "<input style='width:100%' name='itemquantity" + (numberOfRows-1) + "' required/>";
	cell3.innerHTML = "<button id = '" + numberOfRows + "' onclick='deleteRowNewList(" + numberOfRows + ")'>Delete</button>";
    
}
function addRowViewList() {
	var numberOfRows = document.getElementById("viewListTable").rows.length;
    var table = document.getElementById("viewListTable");
    var row = table.insertRow(numberOfRows);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
	var cell3 = row.insertCell(2);
		
    cell1.innerHTML = "<input style='width:100%'/>";
    cell2.innerHTML = "<input style='width:100%'/>";
	cell3.innerHTML = "<button id = '" + numberOfRows + "' onclick='deleteRowViewList(" + numberOfRows + ")'>Delete</button>";	
}

function updateList(myTable) {
    
}

function deleteRowNewList(rowToDelete) {
	var numberOfRows = document.getElementById("newListTable").rows.length;
		
	for(var i=rowToDelete; i < numberOfRows - 1; i++){	
		var row = document.getElementById("newListTable").rows[i+1];
		var cell = row.cells.item(2);
		cell.innerHTML = "<button id = '" + i + "' onclick='deleteRowNewList(" + i + ")'>Delete</button>";
	}
		
    document.getElementById("newListTable").deleteRow(rowToDelete);
}

function deleteRowViewList(rowToDelete) {	
	var numberOfRows = document.getElementById("viewListTable").rows.length;
		
	for(var i=rowToDelete; i < numberOfRows - 1; i++){	
		var row = document.getElementById("viewListTable").rows[i+1];
		var cell = row.cells.item(2);
		cell.innerHTML = "<button id = '" + i + "' onclick='deleteRowViewList(" + i + ")'>Delete</button>";
	}
		
    document.getElementById("viewListTable").deleteRow(rowToDelete);
	
}
