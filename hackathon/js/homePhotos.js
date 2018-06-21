$(document).ready(function () {
    $.get("/all_photos", function (data) {
        response = JSON.parse(data)
        console.log(response);
        for (var i = 0; i < response.photos.length; i++) {
            var newImage = $("<img>");
            newImage.attr("src",response.photos[i].imgURL);
            newImage.addClass("displayedPhotos");
            $(".allPhotos").append(newImage);
        };
    });

});

