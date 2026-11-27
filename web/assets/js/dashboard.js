"use strict";
function parseDecimal(v) {
  if(typeof v!=="string"||!/^[0-9]{1,12}(?:[.,][0-9]{1,6})?$/.test(v)) throw Error("invalid");
  const [a,b=""]=v.replace(",",".").split(".");
  return BigInt(a)*1000000n+BigInt(b.padEnd(6,"0"));
}

function decimalText(n,d) {
  const s=(n<0n?-n:n).toString().padStart(d+1,"0");
  return (n<0n?"-":"")+s.slice(0,-d)+"."+s.slice(-d);
}

function ratio2(n,d) {
  if(d<=0n||n<0n)throw Error("invalid");
  return decimalText((n*200n+d)/(2n*d),2);
}

function budget(income,expense) {
  const i=parseDecimal(income),e=parseDecimal(expense);
  return {balance:decimalText(i-e,6).replace(/0+$/,"").replace(/\.$/,""),share:i===0n?null:ratio2(e*100n,i)};
}

function work(net,hours,cost) {
  const n=parseDecimal(net),h=parseDecimal(hours),c=parseDecimal(cost);
  return {rate:ratio2(n,h),equivalent:ratio2(c*h,n*1000000n)};
}

function mount(doc) {
  const el=id=>doc.getElementById(id);
  if(!el("dashboard-mode"))return;
  const fields={budget:["income","expense"],time:["net","hours","cost"]};
  const results={budget:["balance","share"],time:["rate","equivalent"]};
  function show() {
    for(const m of ["budget","pps","time"])el("panel-"+m).hidden=el("dashboard-mode").value!==m;
  }
  function refresh(m) {
    const p=el("panel-"+m),currency=el(m+"-country").value==="PL"?"PLN":"EUR";
    el(m+"-currency").textContent=currency;
    el(m+"-results").hidden=true;
    for(const k of results[m])el(m+"-"+k).textContent="—";
    const v=fields[m].map(k=>el(m+"-"+k).value),msg=el(m+"-message");
    if(v.some(x=>x==="")){msg.textContent=p.dataset.blank;return;}
    try {
      const r=m==="budget"?budget(...v):work(...v);
      for(const k of results[m]){
        const unit=k==="share"?"%":k==="equivalent"?"h":k==="rate"?currency+"/h":currency;
        el(m+"-"+k).textContent=r[k]===null?p.dataset.undefined:(doc.documentElement.lang==="en"?r[k]:r[k].replace(".",","))+" "+unit;
      }
      msg.textContent=p.dataset.sim;el(m+"-results").hidden=false;
    }catch(_){msg.textContent=p.dataset.invalid;}
  }
  function clear(m){for(const k of fields[m])el(m+"-"+k).value="";refresh(m);}
  el("dashboard-controls").hidden=false;el("dashboard-mode").addEventListener("change",show);
  for(const m of ["budget","time"]){
    el(m+"-controls").hidden=false;
    for(const k of fields[m])el(m+"-"+k).addEventListener("input",()=>refresh(m));
    for(const k of (m==="budget"?["country","period","basis"]:["country","period"]))el(m+"-"+k).addEventListener("change",()=>clear(m));
    el(m+"-clear").addEventListener("click",()=>clear(m));refresh(m);
  }
  el("pps-category").addEventListener("change",()=>{el("pps-selected").textContent=el("pps-category").value;});
  el("pps-controls").hidden=false;show();
}

if (typeof module !== "undefined" && module.exports) module.exports = {parseDecimal,budget,work,mount};
if (typeof document !== "undefined") mount(document);
