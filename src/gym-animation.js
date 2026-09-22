// Authored pose atlases keep hands on the bar and feet on the treadmill belt.
function gymPose(name,index,x,footY,standingHeight,referenceHeight,rotation=0,flip=1){
  const r=RECTS[name][index],h=standingHeight*r[3]/referenceHeight;
  sprite(name,index,x,footY,h,rotation,flip);
}
function gymBulk(t){
  const inflation=(t<signatureCelebrateUntil?.12:0)+.36*Math.pow(progress(),1.25)+(t<gymWobbleUntil&&!prefs.motion?Math.sin(t/45)*.045:0),plopAge=age('plop',t);
  const deflation=plopAge<0?0:prefs.motion?1:ease(plopAge/.9);
  return {inflation,deflation,chestScale:1+inflation-(.48+inflation)*deflation};
}
function gym(t){drawSignature(t);
  const lower=age('lower',t),flee=age('lifter',t),trainerEscape=age('trainer',t),blast=age('blast',t),run=age('runner',t),plopAge=age('plop',t);
  const elapsed=Math.max(0,t-roundStart),moving=state==='playing'||state==='ending'||state==='done';
  const curlSequence=[0,0,1,2,2,1],curlFrame=prefs.motion||!moving?0:curlSequence[Math.floor(elapsed/220)%curlSequence.length];
  const lifterFrame=flee>=0?4+(prefs.motion?0:Math.floor(flee*8)%2):lower>=0?3:curlFrame;
  const lifterX=190-(flee>=0?ease(flee/1.3)*420:0),floor=783;
  if(flee<1.6)gymPose('lifter',lifterFrame,lifterX,floor,264,467,0,lifterFrame===5?-1:1);
  // He sets the bar down before leaving it behind on the platform.
  if(flee>=0)barbell(190,776);
  const trainerX=935+(trainerEscape>=0?ease(trainerEscape/1.2)*440:0);
  const trainerFrame=trainerEscape>=0?3+(prefs.motion?0:Math.floor(trainerEscape*9)%2):blast>=0?2:progress()>.22?1:(prefs.motion?0:Math.floor(elapsed/1800)%2);
  if(trainerEscape<1.4)gymPose('trainer',trainerFrame,trainerX,790,235,490,0);
  if(blast>=0){
    const flight=clamp(blast/1.6),x=976+flight*125,y=605-160*Math.sin(flight*Math.PI)+flight*175;
    sprite('trainer',5,x,y,58,prefs.motion?0:Math.min(blast,1.6)*5);
  }
  // The belt and feet share a ground plane. Strides speed up as strain builds.
  const strideMs=run>=0?83:Math.max(120,205-progress()*75),runnerFrame=prefs.motion?1:Math.floor(elapsed/strideMs)%4;
  const beltY=589;
  ctx.save();ctx.beginPath();ctx.moveTo(966,545);ctx.lineTo(1135,565);ctx.lineTo(1173,606);ctx.lineTo(1000,580);ctx.closePath();ctx.clip();
  const beltOffset=prefs.motion?0:(elapsed/(run>=0?2:4))%30;
  for(let i=-2;i<10;i++)line([[955+i*30+beltOffset,542],[995+i*30+beltOffset,610]],'#789398',2);
  ctx.restore();
  if(plopAge<0){
    gymPose('runner',runnerFrame,1075,beltY,223,496,0,runnerFrame===3?-1:1);
    if(run>=0)for(let i=0;i<3;i++)line([[1143,455+i*24],[1185,453+i*24]],'#ffef83',3);
  }else if(plopAge<.72&&!prefs.motion){
    const u=clamp(plopAge/.72),y=beltY+195*u*u;
    gymPose('runner',4,1075+12*u,y,223,496,-Math.sin(u*Math.PI)*.15);
  }else{
    gymPose('runner',5,1087,790,223,496);
  }
  if(age('rattle',t)>=0){for(let i=0;i<3;i++){const a=plopAge>=0?plopAge:0;const x=115+i*50+(a?Math.min(a*90,110):0),y=822-(a&&!prefs.motion?Math.abs(Math.sin(a*7+i))*Math.max(0,100-a*30):0);ctx.save();ctx.translate(x,y);ctx.rotate(prefs.motion?0:a);roundRect(-19,-9,38,18,5,'#615b8b');ctx.restore();}}
  if(age('sign',t)>=0){const a=age('sign',t);ctx.save();ctx.translate(600,80+ease(a)*65);ctx.rotate(prefs.motion?0:Math.sin(t/160)*.04);roundRect(-215,-32,430,64,8,'#edbb39');text(won?'NEW PERSONAL BEST!':'THIS IS NOT A DRILL!',0,12,29);ctx.restore();}
  gymMetrics={lifterFrame,lifterX,trainerFrame,trainerX,runnerFrame:plopAge>=.72?5:plopAge>=0?4:runnerFrame,runnerFootY:plopAge>=.72?790:beltY,barOnFloor:flee>=0,...gymBulk(t)};
}
