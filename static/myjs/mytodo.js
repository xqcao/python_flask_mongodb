var app = angular.module('myApp', []);


app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}); // NEWLY ADDED


app.controller('myCtrl', function($scope) {
  $scope.uname = "hello world";
  $scope.todo = function() {
    console.log('this is clicked' + $scope.uname)
    $scope.msg1 = $scope.uname + " welcome this web 123";
  }
})
