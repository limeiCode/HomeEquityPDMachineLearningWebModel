  // var btn = d3.select('#predict-btn');
  // btn.on("click", function handleClick() {
  
d3.select('#predict-btn').on("click", function handleClick() {
  // d3.event.preventDefault();  // "submit" in a Form need preventDefault() -- click event, change event doesn't need
  
  var input1 = d3.select("#input1").property("value");   
  var input2 = d3.select("#input2").property("value");   
  var input3 = d3.select("#input3").property("value");  
  // d3.select("#stockInput").node().value  // ?? 
  // // console.log(input1);
  console.log(input1);
  console.log(input2);
  console.log(input3);

  // var inputobj = {
  //   input1: input1,
  //   input2: input2,
  //   input3: input3
  // };
  // console.log(inputobj);

  // var inputlst = [ input1, input2, input3 ];
  // console.log(inputlst);

  // inputdata = inputlst;  // ["1", "2", "3"]
  // console.log(inputdata);
  // // d3.json("data/yelp_test_set_business.json", function (error, yelp_data) {
  // // d3.json(`/predictonesample/${inputdata}`).then((items) => {  // ?????????
  d3.json(`/predictonesample/${input1}|${input2}|${input3}`, function(error,items) {     
    var selector = d3.select("#result");
    // selector.innerHTML = 

    console.log(items);
    // selector.text = items
    selector.text(items) ; // should from items ??? 
    // r = items(0); //1 ?
    // selector.innerHTML = r;
    // document.getElementById('lbltipAddedComment').innerHTML = 'your tip has been submitted!';
  });    

});



// function buildMetadata(sample) {   
//   d3.json(`/metadata/${sample}`).then((items) => {    
//       var selector = d3.select("#sample-metadata");
//       selector.html("");
//       Object.entries(items).forEach(([key,value]) => {
//         selector
//           .append("h6")
//           .text(`${key}: ${value}`)
//       });            
//   });     
// };

// function buildCharts(sample) {
//  d3.json(`/samples/${sample}`).then(dataObj => {
//     var otuIdList = dataObj['otu_ids'];
//     var otuValueList = dataObj['sample_values'];
//     var otuLabelList = dataObj['otu_labels']; 
//     var otuIdTop = otuIdList.slice(0,10); //  Top 10 sample values as values 
//     var otuValueTop = otuValueList.slice(0,10);
//     var otuLabelTop = otuLabelList.slice(0,10);
//     var trace1=[{
//       type:'pie', 
//       labels:otuIdTop, //  otu_ids as the labels 
//       values:otuValueTop,
//       hovertext: otuLabelTop, // ✓ otu_labels as the tooltip
//       hoverinfo: "hovertext",
//     }]
//     var layout1 ={
//       height: 400,
//       width: 500,
//       title: "Values of Top 10 Samples"        
//     };
//     Plotly.newPlot("pie",trace1,layout1);        

//     trace2=[{
//       x: otuIdList,       //  otu_ids for the x values
//       y: otuValueList,    //  sample_values for the y values
//       text: otuLabelList, //  otu_labels for text values 
//       mode: 'markers',             
//       marker: {
//         size: otuValueList ,   
//         color: otuIdList,  // ✓ otu_ids for marker colors
//         colorscale: "Earth",  
//       },
//     }]; 
//     var layout2 ={
//       height: 500,
//       width: 1500,    
//       hovermode: "closest",  
//       title:"Values of All Samples",
//       xaxis: {title:"OTU ID"}, 
//     };           
//     Plotly.newPlot("bubble",trace2,layout2);
    
// });
// }

// function init() {
// // Grab a reference to the dropdown select element
//     var selector = d3.select("#selDataset");

//     // Use the list of sample names to populate the select options
//     d3.json("/names").then((sampleNames) => {
//         sampleNames.forEach((sample) => {
//           selector
//             .append("option")
//             .text(sample)
//             .property("value", sample);
//         });

//     // Use the first sample from the list to build the initial plots
//         const firstSample = sampleNames[0];
//         buildCharts(firstSample);
//         buildMetadata(firstSample);
//     });
// }

// function optionChanged(newSample) {
// // Fetch new data each time a new sample is selected
// buildCharts(newSample);
// buildMetadata(newSample);
// }

// // Initialize the dashboard
// init();
