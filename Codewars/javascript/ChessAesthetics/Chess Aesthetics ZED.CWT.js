// author ZED.CWT from codewars.com
get_without_every_piece=Q=>Q.replace(/(\d?)[A-Za-z](?=(\d?)(.*))(?=(.* ){5})/g,($,L,R,U)=>W.push(Q.slice(0,Q.length-U.length-!!L-!!R-1)+(L-~R)+U),W=[])&&W