<?php
/***************************************************************************
 *
 * Copyright (c) 2016 Baidu.inc All Rights Reserved
 *
 **************************************************************************/
 
 
 
/**
 * @file user_sort.php
 * @author 石宽(shikuan@baidu.com)
 * @date 2016/09/28 15:14:00
 * @version $Revision$
 * @brief
 *
 **/

class TestObj {
    var $name;

    function TestObj($name)
    {
        $this->name = $name;
    }

    /* This is the static comparing function: */
    static function cmp_obj($a, $b)
    {
        $al = strtolower($a->name);
        $bl = strtolower($b->name);
        if ($al == $bl) {
            return 0;
        }
        return ($al > $bl) ? +1 : -1;
        // echo $a . "\t" . $b . "\n";
        // if ($a == $b) {
        //     return 0;
        // }
        // return ($a < $b) ? -1 : 1;
    }
}

$a[] = new TestObj("c");
$a[] = new TestObj("b");
$a[] = new TestObj("d");

#$a = array(3, 2, 5, 6, 1);

usort($a, array("TestObj", "cmp_obj"));

foreach ($a as $item) {
    echo $item->name . "\n";
    #echo $item . "\n";
}
?>





