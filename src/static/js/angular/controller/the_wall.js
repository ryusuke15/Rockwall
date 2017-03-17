app = angular.module('wallCtrl', []);

app.controller('wallController',function($http, $scope) {

var token = '2898925426.15bbac2.6e8625119797427a8bf3415e6926bc67'
var address = "https://api.instagram.com/v1/users/self/media/recent/?access_token="

function call(response){
    $scope.photos=response.data.data;
    // console.log(response)  
}

$http.jsonp(' https://api.instagram.com/v1/users/self/media/recent/',{
    params:{
    access_token:'2898925426.15bbac2.6e8625119797427a8bf3415e6926bc67',
    jsonpCallbackParam: 'callback'
}
})
.then(function(response) {
    call(response);
});


 
});
