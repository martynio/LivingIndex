"use strict";
const api=require("../web/assets/js/dashboard.js");
function verify(api) {
 let n=0;function eq(a,b){if(JSON.stringify(a)!==JSON.stringify(b))throw Error(JSON.stringify({a,b}));n++;}
 function rejects(f){let failed=false;try{f();}catch(_){failed=true;}if(!failed)throw Error("Expected rejection");n++;}
 eq(api.budget("2000","1500"),{balance:"500",share:"75.00"});
 eq(api.budget("100","120"),{balance:"-20",share:"120.00"});
 eq(api.budget("0","10"),{balance:"-10",share:null});
 eq(api.budget("0,30","0.10"),{balance:"0.2",share:"33.33"});
 eq(api.budget("0","0"),{balance:"0",share:null});
 eq(api.budget("0.000001","0"),{balance:"0.000001",share:"0.00"});
 eq(api.work("2000","160","100"),{rate:"12.50",equivalent:"8.00"});
 eq(api.work("10","3","100"),{rate:"3.33",equivalent:"30.00"});
 eq(api.work("1","200","0.000025"),{rate:"0.01",equivalent:"0.01"});
 eq(api.work("100","160","0"),{rate:"0.63",equivalent:"0.00"});
 for(const v of ["","-1","1e3","NaN","Infinity","0.0000001","1234567890123",true,1,null])rejects(()=>api.budget("1",v));
 rejects(()=>api.work("0","1","1"));rejects(()=>api.work("1","0","1"));
 return n;
}
console.log("Dashboard arithmetic assertions PASS: "+verify(api));
