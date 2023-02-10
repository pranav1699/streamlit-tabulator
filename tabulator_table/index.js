function onDataFromPython(event) {

  const data = event.detail;

  spec = JSON.parse(data.args.spec);
  console.log(spec);


  var tabledata = spec ;
  
  
  document.getElementById("download-csv").addEventListener("click", function () {
    table.download("csv", "test.csv");
  });

  //define table
  var table = new Tabulator("#example-table", {
    data: tabledata,
    renderHorizontal: "virtual",
    height: "350px",
    movableRows: true,
    // groupBy:"Group",
    // groupStartOpen:false,
    //movableRows: true,
    movableColumns: true,
    autoColumns: true
  });


  Streamlit.setFrameHeight(document.documentElement.clientHeight);
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onDataFromPython);
Streamlit.setComponentReady();