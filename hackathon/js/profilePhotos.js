$(document).ready(function () {
    $.get("/profile_photos", function (data) {
        response = JSON.parse(data)
        for (var i = 0; i < response.photos.length; i++) {
            var newImage = $("<img>");
            newImage.attr("src",response.photos[i].imgURL);
            newImage.addClass("displayedPhotos");
            $("#myProfilePictures").append(newImage);
        };
    });

});

