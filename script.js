// =========================
// DRAG & DROP
// =========================

let draggedAgent = null;

const agentCards =
document.querySelectorAll(".agentCard");

const slots =
document.querySelectorAll(".slot");

agentCards.forEach(card=>{

card.addEventListener(
"dragstart",
()=>{

draggedAgent = card;

card.classList.add(
"dragging"
);

});

card.addEventListener(
"dragend",
()=>{

card.classList.remove(
"dragging"
);

});

});

slots.forEach(slot=>{

slot.addEventListener(
"dragover",
e=>{

e.preventDefault();

slot.classList.add(
"hover"
);

});

slot.addEventListener(
"dragleave",
()=>{

slot.classList.remove(
"hover"
);

});

slot.addEventListener(
"drop",
()=>{

slot.classList.remove(
"hover"
);

if(!draggedAgent)
return;

slot.innerHTML =
draggedAgent.innerHTML;

slot.dataset.agent =
draggedAgent.dataset.agent;

slot.classList.add(
"filled"
);

});

});

// =========================
// MISSION
// =========================

const requiredAgents = [

"search",
"planner",
"budget",
"communication",
"memory"

];

const launchBtn =
document.getElementById(
"launchBtn"
);

launchBtn.addEventListener(
"click",
launchMission
);

function launchMission(){

const log =
document.getElementById(
"log"
);

log.innerHTML = "";

const chosenAgents = [];

slots.forEach(slot=>{

if(slot.dataset.agent){

chosenAgents.push(
slot.dataset.agent
);

}

});

// =========================
// CHECK MISSING AGENTS
// =========================

for(let agent of requiredAgents){

if(
!chosenAgents.includes(
agent
)
){

showFailure(agent);

return;

}

}

// =========================
// SUCCESS PATH
// =========================

document.getElementById(
"commanderSpeech"
).innerHTML =
"Excellent team. Launching mission!";

runMission();

}

// =========================
// FAILURE SCREEN
// =========================

function showFailure(
missingAgent
){

const log =
document.getElementById(
"log"
);

let reason = "";

if(
missingAgent==="memory"
){

reason =
"🤖 I forgot our previous findings!";

}

else if(
missingAgent==="planner"
){

reason =
"😵 Nobody planned the mission!";

}

else if(
missingAgent==="search"
){

reason =
"🔍 Nobody searched for resources!";

}

else if(
missingAgent==="budget"
){

reason =
"💰 No budget calculation done!";

}

else if(
missingAgent==="communication"
){

reason =
"📡 Nobody sent the report to Earth!";

}

log.innerHTML =

`
<div class="failure">

🚨 MISSION FAILED

<br><br>

Missing Agent:

${missingAgent.toUpperCase()}

<br><br>

${reason}

</div>
`;

document.getElementById(
"commanderSpeech"
).innerHTML =
"Mission Failed 😭";

}

// =========================
// TASK ANIMATION
// =========================

function createTaskBubble(
text
){

const bubble =
document.createElement(
"div"
);

bubble.className =
"taskBubble";

bubble.innerHTML =
text;

bubble.style.left =
"20px";

bubble.style.top =
Math.random()*120+"px";

document
.getElementById(
"taskArea"
)
.appendChild(
bubble
);

setTimeout(()=>{

bubble.style.left =
"90%";

},100);

setTimeout(()=>{

bubble.remove();

},2200);

}

// =========================
// RUN MISSION
// =========================

function runMission(){

const log =
document.getElementById(
"log"
);

const tasks = [

{
task:
"🔍 Research Resources",
msg:
"Resources found on Mars"
},

{
task:
"📅 Survival Plan",
msg:
"Survival plan created"
},

{
task:
"💰 Budget",
msg:
"Budget calculated"
},

{
task:
"📡 Report To Earth",
msg:
"Report sent successfully"
},

{
task:
"🧠 Remember Findings",
msg:
"Findings stored in memory"
}

];

tasks.forEach(
(item,index)=>{

setTimeout(()=>{

createTaskBubble(
item.task
);

log.innerHTML +=

`
<div>

${item.task}
✅

</div>
`;

},index*2500);

});

setTimeout(()=>{

missionSuccess();

},tasks.length*2500+1000);

}

// =========================
// SUCCESS
// =========================

function missionSuccess(){

const log =
document.getElementById(
"log"
);

log.innerHTML +=

`
<br>

<div class="success">

🚀 MARS COLONY ESTABLISHED

<br><br>

MISSION SUCCESS

</div>
`;

document.getElementById(
"commanderSpeech"
).innerHTML =
"Mission Accomplished 🎉";

showFileReveal();

}

// =========================
// REVEAL FILES
// =========================

function showFileReveal(){

setTimeout(()=>{

document.getElementById(
"revealPanel"
).style.display =
"block";

},1500);

}