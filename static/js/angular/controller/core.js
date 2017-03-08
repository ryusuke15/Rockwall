var RockwallApp = angular.module('Rockwall', [
    'wallCtrl',
]);

RockwallApp.config([
    '$interpolateProvider','$sceDelegateProvider', function($interpolateProvider, $sceDelegateProvider){
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
        $sceDelegateProvider.resourceUrlWhitelist([
            'self',
            'https://api.instagram.com/v1/users/self/media/recent/**'
        ])
    }

]);
