var News = angular.module("News", [],
    function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");    }

);
News.config(['$httpProvider', function($httpProvider) {
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
}
]);

News.factory('NewsService', function ($http, $q) {
    var api_url = '/';
    return {
        get: function (news_id) {
            var url = api_url + news_id + "/";
            var defer = $q.defer();
            $http({method: 'GET', url: url}).
                success(function (data, status, headers, config) {
                    defer.resolve(data);
                })
                .error(function (data, status, headers, config) {
                    defer.reject(status);
                });
            return defer.promise;
        },
        query: function(q_url,text){
            if (typeof text === 'undefined'){               
                text = "";
            }
            var url = api_url + 'page_size=' + num + '&q=' + text ;
            var defer = $q.defer();
            $http({method: 'GET', url: url}).
                success(function(data, status, headers, config) {
                    defer.resolve(data);
                }).
                error(function(data, status, headers, config) {
                    defer.reject(status);

                });
            return defer.promise;
        }

    }
});



News.controller('NewsController', ['$scope','$routeParams','NewsService', '$location', function ($scope,$routeParams,NewsService, $location) {
     $scope.search =function(keywords){
        var url = "/search/" + keywords;
        $location.path(url)
    };

    //For showing search item name in template//
//    $scope.location = $location.path();
//    var position = $scope.location.indexOf('/',1);
//    $scope.item = $scope.location.substring(position +1);

}]);