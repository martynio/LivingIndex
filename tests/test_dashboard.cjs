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

// Minimal DOM model: event wiring, independent panel state and no stale results.
function verifyControls(api) {
  let n=0;
  function check(ok){if(!ok)throw Error("Dashboard control assertion failed: "+n);n++;}
  for(const lang of ["en","pl","nl"]){
    const nodes=new Map();
    const get=id=>{
      if(!nodes.has(id))nodes.set(id,{value:"",textContent:"",hidden:true,dataset:{blank:"blank",invalid:"invalid",undefined:"undefined",sim:"simulation"},events:{},addEventListener(k,f){this.events[k]=f;}});
      return nodes.get(id);
    };
    const change=(id,v,event="change")=>{get(id).value=v;get(id).events[event]();};
    get("dashboard-mode").value="budget";
    get("budget-country").value=get("time-country").value="PL";
    api.mount({getElementById:get,documentElement:{lang}});
    check(!get("panel-budget").hidden&&get("panel-pps").hidden&&get("panel-time").hidden);
    check(get("budget-results").hidden);
    change("budget-income","2000","input");change("budget-expense","1500","input");
    check(get("budget-balance").textContent==="500 PLN"&&!get("budget-results").hidden);
    change("budget-country","NL");check(get("budget-income").value===""&&get("budget-results").hidden&&get("budget-currency").textContent==="EUR");
    change("budget-income","0","input");change("budget-expense","10","input");check(get("budget-share").textContent==="undefined");
    change("dashboard-mode","pps");check(!get("panel-pps").hidden&&get("panel-budget").hidden);
    change("pps-category","CP12");check(get("pps-selected").textContent==="CP12");
    change("dashboard-mode","time");check(!get("panel-time").hidden&&get("panel-pps").hidden);
    change("time-net","2000","input");change("time-hours","160","input");change("time-cost","100","input");
    check(get("time-equivalent").textContent===(lang==="en"?"8.00 h":"8,00 h"));
    change("time-hours","0","input");check(get("time-results").hidden&&get("time-message").textContent==="invalid"&&get("time-equivalent").textContent==="—");
    change("time-hours","160","input");change("time-period","year");check(get("time-net").value===""&&get("time-results").hidden);
    change("dashboard-mode","budget");check(get("budget-income").value==="0"&&get("budget-expense").value==="10");
    get("budget-clear").events.click();check(get("budget-results").hidden&&get("budget-expense").value==="");
  }
  return n;
}
console.log("Dashboard mock-DOM assertions PASS: "+verifyControls(api));
