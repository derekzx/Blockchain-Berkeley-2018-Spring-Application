var express = require("express");
var http = require("http").Server(app);
var fs =require('fs')
var app = express();
var router = express.Router();
var path = __dirname + '/views/';
var path = require('path')


router.use(function (req,res,next) {
  console.log("/" + req.method);
  next();
});

router.get("/",function(req,res){
  res.sendFile(__dirname + "/public/templates/index.html");
  console.log('Showing Index')
});

router.get("/topicsMain",function(req,res){
  res.sendFile(__dirname + "/public/templates/pages/topicsMain.html");
  console.log("Showing topicsMain page")
});

router.get("/economics",function(req,res){
  res.sendFile(__dirname + "/public/templates/pages/forumEconomics.html");
  console.log('Showing forum page (economics)')
});

router.get("/netNeutrality",function(req,res){
  res.sendFile(__dirname + "/public/templates/pages/forumThread.html");
  console.log('Showing forum page (netNeutrality)')
});


app.use("/",router);
// app.use('/public', express.static("/" + '/public'));
app.use(express.static(path.join(__dirname, 'public')));

// app.use("*",function(req,res){
//   res.sendFile(path + "404.html");
// });

app.listen(3000,function(){
  console.log("Live at Port 3000");
});
