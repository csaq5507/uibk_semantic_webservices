<?php
/**
 *
 * Created by PhpStorm.
 * User: ivan
 * Date: 20.06.18
 * Time: 20:33
 */

error_reporting(E_ALL);
ini_set('display_errors', 1);
include_once('http.php'); //where HttpRequest.php is the saved file

$base_url = "http://localhost:5000";


function entry_points($result){
    echo '<a href="?url='.$result->{'events'} .'" >Events</a><br>';
}

function event_collection($result){
    $events = $result->{"members"};
    for($i = 0; $i < count($events); $i++)
    {
        echo '<a href="?url='.$events[$i]->{"@id"}.'" >Event '.($i+1).'</a> <br>';
    }
}
if(isset($_GET["url"]))
    $url = $_GET["url"];
else
    $url = "/api";

if(isset($_GET["method"]))
    $method = $_GET["method"];
else
    $method = "GET";

$r = new HttpRequest($base_url.$url, $method);
try {
    $r->send();
    if ($r->getStatus() == 200) {
        $result = json_decode($r->getResponseBody());
        if($result->{'@type'} == "EntryPoint")
            entry_points($result);
        if($result->{'@type'} == "EventCollection")
            event_collection($result);
        if($result->{'@type'} == "Event")
            show_event($result);

    } else
        echo "Api not reachable. ".$r->getStatus();

} catch (HttpException $ex) {
    echo $ex;
}




?>
