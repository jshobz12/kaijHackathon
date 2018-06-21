$(document).ready(function () {
    $.get("/scores", function (data) {
        response = JSON.parse(data);
        var tab = $("<tr></tr>");
        var ranking = $("<th></th>");
        var username = $("<th></th>");
        var points = $("<th></th>");
        var instagram = $("<th></th>");
        ranking.text("Ranking");
        username.text("Username");
        points.text("Points");
        instagram.text("Instagram");
        tab.append(ranking);
        tab.append(username);
        tab.append(points);
        tab.append(instagram);
        $("#myTable").append(tab);
        for (var i = 0; i < response.scores.length; i++) {
            var newPlayer = $("<tr></tr>");
            var playerRanking = $("<th></th>");
            var playerName = $("<th></th>");
            var playerPoints = $("<th></th>");
            var playerProfile = $("<th></th>");
            playerRanking.text(i+1);
            playerName.text(response.scores[i].username);
            playerPoints.text(response.scores[i].totalpts);
            playerProfile.text("@"+response.scores[i].handle);
            newPlayer.append(playerRanking);
            newPlayer.append(playerName);
            newPlayer.append(playerPoints);
            newPlayer.append(playerProfile);
            $("#myTable").append(newPlayer);
        }
    });

});

