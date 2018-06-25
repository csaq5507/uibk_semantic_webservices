<html>
<head>
    <title>Hydra Api Client</title>
</head>
<body>


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

$entry_point = "/api";

$url = null;
$vocab = null;

if(isset($_POST["met"]) && isset($_POST["url"]))
{
    $r = new \JJG\Request($_POST["url"]);
    $r->setRequestType($_POST["met"]);
    $r->setRequestHeader("Content-Type: application/json");
    $r->setRequestHeader("Accept: application/json");
    if($_POST["met"] == "POST" || $_POST["met"] == "PUT" )
    {
        $post = array();
        foreach ($_POST as $key=>$value)
        {
            if($key == "url" || $key == "met")
                continue;
            else
                $post[$key]=$value;
        }
        $data_json = json_encode($post);
        $r->setPostFields($data_json);
    }

    try {
        $r->execute();
        if ($r->getHttpCode() == 200) {
            $result = json_decode($r->getResponse());
            if($result->{"@type"} == "EntryPoint")
            {
                $url = $result->{"events"};
                ?>
                <script type="text/javascript">
                    document.getElementsByTagName("body")[0].onload = function() {
                        document.getElementById("class_picker").selectedIndex = 3;
                        makeVisible(document.getElementById("class_picker"));
                    }

                </script>
                <?php
            } else if($result->{"@type"}=="EventCollection")
            {
                $events=$result->{"members"};
                ?>
                <script type="text/javascript">
                    function updateURL(url){
                        var elems = document.getElementsByName("url");
                        document.getElementById("class_picker").selectedIndex=1;
                        makeVisible(document.getElementById("class_picker"));
                        for(var i=0; i<elems.length;i++)
                        {
                            elems[i].value="<?php echo $base_url; ?>"+url;
                        }
                    }
                </script>

                <table>
                    <tr>
                <?php
                for($i=0;$i<count($events);$i++)
                {
                                        $ev = (array) $events[$i];
                    echo "<td>";
                    foreach ($ev as $p_name=>$p_value)
                    {
                        if($p_name=="@id") {
                            ?>
                            <a href="javascript:updateURL('<?php echo $p_value; ?>')"><?php echo $p_value; ?></a><br>
                            <?php
                        } else
                                echo "$p_name: $p_value<br>";

                    }
                    echo "</td>";
                    if($i%5==4)
                        echo "</tr><tr>";
                }
                ?>
                    </tr>
                </table>
                <?php
            } else if($result->{"@type"}=="Event")
            {

            }
        } else if($r->getHttpCode() == 201)
        {
            echo "Success!<br>";
            $result = json_decode($r->getResponse());


                $ev = (array) $result;
                foreach ($ev as $p_name=>$p_value)
                {
                    if($p_name=="@id") {
                        ?>
                        <a href="javascript:updateURL('<?php echo $p_value; ?>')"><?php echo $p_value; ?></a><br>
                        <?php
                } else
                    echo "$p_name: $p_value<br>";

                }



        } else if($r->getHttpCode() == 400) {
            echo $r->getResponse();
        } else {
            echo "Api not reachable. ".$r->getHttpCode();
        }
    }catch (HttpException $ex) {
        echo $ex;
    }
} else $url = $entry_point;

$r = new \JJG\Request($base_url.$entry_point);
$r->setRequestType( "GET");
try {
    $r->execute();
    if ($r->getHttpCode() == 200) {
        $result = get_object_vars(json_decode($r->getResponse()));
        $headers = $r->getHeader();
        //$link = $headers["link"];
        $vocab = "http://localhost:5000/api/vocab"; //TODO cant get vocab from server!!!
    } else
        echo "Api not reachable. ".$r->getHttpCode();
}catch (HttpException $ex) {
    echo $ex;
}

$r1 = new \JJG\Request($vocab);
$r1->setRequestType("GET");
try {
    $r1->execute();
    if ($r1->getHttpCode() == 200) {
        $result = json_decode($r1->getResponse());
        echo "Vocab found.<br>";
        $support=$result->{"supportedClass"};
        ?>
        <script type="text/javascript">
            function makeVisible(elem)
            {
                for(var a=1;a<elem.children.length;a++)
                    document.getElementById(elem.children[a].value).style.display = "none";
                document.getElementById(elem.children[elem.selectedIndex].value).style.display = "block";
            }

        </script>

        <select id="class_picker" onchange="makeVisible(this)">
            <option value="">Please Select...</option>
            <?php
            for($i = 0; $i< count($support);$i++) {
                $ops = $support[$i]->{"supportedOperation"};
                if (count($ops) != 0) {
                    if (property_exists($support[$i], "hydra:title"))
                        $title = $support[$i]->{"hydra:title"};
                    else if (property_exists($support[$i], "label"))
                        $title = $support[$i]->{"label"};
                    echo "<option value='".$support[$i]->{"@id"}."' >$title</option>";
                }
            }
            ?>
        </select>
        <?php
        for($i = 0; $i< count($support);$i++)
        {
            $ops = $support[$i]->{"supportedOperation"};

                if(count($ops) != 0) {

                echo "<div id='".$support[$i]->{"@id"}."' style='display: none;'>";

                if(property_exists($support[$i],"hydra:title"))
                    echo "<h2>".$support[$i]->{"hydra:title"}."</h2>";
                else if (property_exists($support[$i],"label"))
                    echo "<h2>".$support[$i]->{"label"}."</h2>";

                ?>
                <select onchange="makeVisible(this)">
                    <option value="">Please Select...</option>
                    <?php
                    for($j=0;$j<count($ops);$j++) {
                        echo "<option value='".$ops[$j]->{"@id"}."'>". $ops[$j]->{"label"}."</option>";
                    }
                    ?>
                </select>
                <?php

                for($j=0;$j<count($ops);$j++) {
                    echo "<div id='".$ops[$j]->{"@id"}."' style='display: none;'>";
                    echo "<p>" . $ops[$j]->{"label"} . "</p>";
                    if ($ops[$j]->{"expects"} == null) {

                        ?>
                        <form method='POST'>
                            <label for'url'>URL: </label>
                            <input type='text' name='url' value='<?php echo $base_url.$url; ?>'><br>
                            <label for'met'>Method: </label>
                            <input type='text' name='met' value='<?php echo $ops[$j]->{"method"}; ?>'><br>
                            <input type='submit' value='Go' >
                        </form>
                        <?php
                    } else {
                        $class = null;
                        for($k=0;$k<count($support);$k++)
                        {
                            if($support[$k]->{"@id"} === $ops[$j]->{"expects"})
                            {
                                $class = $support[$k];
                                break;
                            }
                        }
                        if($class == null)
                            echo "An error occured";
                        else {
                            ?>
                            <form method='POST'>
                                <label for'url'>URL: </label>
                                <input type='text' name='url' value='<?php echo $base_url.$url; ?>'><br>
                                <label for'met'>Method: </label>
                                <input type='text' name='met' value='<?php echo $ops[$j]->{"method"}; ?>'><br>
                                <?php
                                for($l=0;$l<count($class->{"supportedProperty"});$l++)
                                {
                                    $p = $class->{"supportedProperty"}[$l];
                                    echo "<label for='".$p->{"hydra:title"}."'>".$p->{"hydra:description"}."</label><br>";
                                    echo "<input type='text' name='".$p->{"hydra:title"}."' ><br>";
                                }
                                ?>
                            <input type='submit' value='Go' >
                            </form>
                            <?php
                        }
                        echo "<br><br>";

                    }
                    echo "</div>";
                }
                echo "</div>";
            }
        }
    } else
        echo "Api not reachable. ".$r1->getHttpCode()."<br>".$r1->getResponse();

} catch (HttpException $ex) {
    echo $ex;
}

?>


</body>
</html>
