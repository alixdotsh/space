module.exports = message => {
	const user = message.mentions.users.first();
	if (user) {
		const member = message.guild.member(user);
		if (member) {
			member
				.kick(`Kicked by Nurple`)
				.then(() => {
					message.reply(`I have used the kick hammer on ${user.tag}!`);
				})
				.catch(err => {
					// If the error happens, most likely because they do not have the permission to kick or they are missing permissions
					message.reply(`I was not able to use the kick hammer! I may not have permissions to do so`)
					console.error(err);
				});
		} else {
			//The user is not in this guild
			message.reply(`That user does nto exist in this guild!`)
		}
		//If no user was mentioned at all
	} else {
		message.reply(`You did not tell me who to kick!`)
	}
}
