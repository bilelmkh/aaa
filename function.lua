ESX.Game.SpawnVehicle = function(modelName, coords, heading, cb)
	local model = (type(modelName) == 'number' and modelName or GetHashKey(modelName))

	Citizen.CreateThread(function()
		ESX.Streaming.RequestModel(model)

		local vehicle = CreateVehicle(model, coords.x, coords.y, coords.z, heading, true, false)
		local networkId = NetworkGetNetworkIdFromEntity(vehicle)
		local timeout = 0

		SetNetworkIdCanMigrate(networkId, true)
		SetEntityAsMissionEntity(vehicle, true, false)
		SetVehicleHasBeenOwnedByPlayer(vehicle, true)
		SetVehicleNeedsToBeHotwired(vehicle, false)
		SetVehRadioStation(vehicle, 'OFF')
		SetModelAsNoLongerNeeded(model)
		RequestCollisionAtCoord(coords.x, coords.y, coords.z)

		-- we can get stuck here if any of the axies are "invalid"
		while not HasCollisionLoadedAroundEntity(vehicle) and timeout < 2000 do
			Citizen.Wait(0)
			timeout = timeout + 1
		end

		if cb then
			cb(vehicle)
		end
	end)
end
